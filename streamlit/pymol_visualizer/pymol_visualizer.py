import streamlit as st
import py3Dmol
from stmol import showmol
from utils import pdb_parser
import re
from urllib import request
import gzip

# TODO:
# * select by resi


st.set_page_config(
    page_title='Pymol Visualizer',
    page_icon=':atom_symbol:',
    layout='wide'
)

# st.markdown('#### :atom_symbol:  Pymol Visualizer  :atom_symbol:')
mobile_size = st.checkbox('Optimize size for mobile?', value=False)

# globals
width = 250 if mobile_size else 600
height = 250 if mobile_size else 400

col1, col2 = st.columns([1,2])
with col1:
    pdb = st.text_input('Enter PDB code:')
    pdb = pdb.strip()

with col2:
    selected_pdb = st.selectbox('Or pick from defaults:', options=('(None)', 'LegH', 'Soy 11S', 'Soy 7S'))
    if selected_pdb == 'LegH':
        pdb = '1FSL'
    elif selected_pdb == 'Soy 11S':
        pdb = '1OD5'
    elif selected_pdb == 'Soy 7S':
        pdb = '1UIK'

if pdb:
    url1 = f'https://files.rcsb.org/download/{pdb}.pdb1.gz'
    file_name1 = re.split(pattern='/', string=url1)[-1]
    r1 = request.urlretrieve(url=url1, filename=file_name1)
    txt1 = re.split(pattern=r'\.', string=file_name1)[0] + '.txt'

    with gzip.open(file_name1, 'rt') as f_in:
        bio_assembly = f_in.readlines()
        parsed_pdb = ''
        for line in bio_assembly:
            if line.startswith('ATOM'):
                parsed_pdb += line

    view = py3Dmol.view(width=width, height=height)
    view.addModelsAsFrames(parsed_pdb)
    view.setStyle({'model': -1}, {'cartoon': {'color': 'spectrum'}})

    # display pdb element title
    st.markdown(f'**[{pdb.upper()}](https://www.rcsb.org/structure/{pdb.upper()}): {pdb_parser.get_name(pdb)}**')

    chains, sequence = pdb_parser.parse_pdb(bio_assembly)

st.sidebar.header('Select options:')
color_selector = st.sidebar.selectbox('Select color from picker or from pymol defaults:', ('Spectrum', 'Color by Chain', 'Color Picker',))
spinning = st.sidebar.selectbox('Set model spin', ('False', 'True'))

if pdb:
    if color_selector == 'Color Picker':
        color = st.sidebar.color_picker('Select color from picker:', value='#00f900')
        view.setStyle({'model': -1}, {'cartoon': {'color': color}})
    elif color_selector == 'Color by Chain':
        colors = ['green', 'cyan', 'magenta', 'yellow', 'wheat', 'slate', 'grey', 'lightpink', 'blue', 'red']
        for idx, c in enumerate(chains):
            view.setStyle({'chain': c}, {'cartoon': {'color': colors[idx]}})
    elif color_selector:
        color = color_selector.lower()
        view.setStyle({'model': -1}, {'cartoon': {'color': color}})

    if spinning == 'True':
        spin_axis = st.sidebar.selectbox('Which axis?', ('x', 'y', 'z'))
        speed = st.sidebar.slider('How fast? (Default is 1)', min_value = 0.5, max_value=3., value=1., step=0.5)
        spin_reverse = st.sidebar.selectbox('Reverse?', ('False', 'True'))
        spin_direction = 1.0 if spin_reverse == 'False' else -1.0
        view.spin(spin_axis, speed * spin_direction)

    button = st.sidebar.button('Reset view', on_click=view.zoomTo)

# center the title
st.markdown('<style>.e16nr0p30 {text-align: center;}</style>', unsafe_allow_html=True)

# adjust the view size and add a border
st.markdown('<style>iframe {border: solid; display: block; margin-left: auto; margin-right: auto; padding-left: 0px;}</style>', unsafe_allow_html=True)

if pdb:
    view.zoomTo()
    view.show()

    showmol(view, width=width, height=height)