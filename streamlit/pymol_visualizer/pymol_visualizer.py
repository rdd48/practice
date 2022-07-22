import streamlit as st
import py3Dmol
from stmol import showmol
import re
from urllib import request
import gzip

# local files
from utils import utils
from pdb_info import pdb_names_dict

# TODO:
# * select by resi (multiselect)
# * save/render images
# * save/render gifs
# * clean up code
# * host on IF github

st.set_page_config(
    page_title='Pymol Visualizer',
    page_icon=':atom_symbol:',
    layout='wide'
)

if 'pdb_state' not in st.session_state:
    st.session_state.pdb_state = None

def set_pdb_state(code):
    if code in ('rcsb_code', 'user_input', 'rcsb_desc'):
        st.session_state.pdb_state = code
    else:
        st.session_state.pdb_state = None

# st.markdown('#### :atom_symbol:  Pymol Visualizer  :atom_symbol:')
mobile_size = st.checkbox('Optimize size for mobile?', value=False)

# globals
width = 250 if mobile_size else 600
height = 250 if mobile_size else 400

col1, col2, col3 = st.columns([1,1,1])

# col1, col2 = st.columns([1,2])
with col1:
    defaults_to_pdb = {
        'LegH': '1FSL',
        'Soy 11S': '1OD5',
        'Soy 7S': '1UIK',
        'Bovine Hemoglobin': '2QSP'
    }
    selected_pdb = st.selectbox('Pick from common options:', options=['', *defaults_to_pdb.keys()], on_change=set_pdb_state, args=['user_input'])

with col2:
    rcsb_input = st.text_input('Or enter PDB code:', on_change=set_pdb_state, args=['rcsb_code'])
    rcsb_input = rcsb_input.strip()

with col3:
    rcsb_desc = st.selectbox('Or search by protein name (slightly laggy)', options=[*pdb_names_dict.all_pdbs_dict.keys()], on_change=set_pdb_state, args=['rcsb_desc'])

if st.session_state.pdb_state == 'rcsb_code':
    pdb = rcsb_input.strip().upper()
elif st.session_state.pdb_state == 'user_input' and selected_pdb:
    pdb = defaults_to_pdb[selected_pdb].strip().upper()
elif st.session_state.pdb_state == 'rcsb_desc':
    pdb = pdb_names_dict.all_pdbs_dict[rcsb_desc]
else:
    pdb = None

st.sidebar.header('Select options:')
color_selector = st.sidebar.selectbox('Select color from picker or from pymol defaults:', ('Spectrum', 'Color by Chain', 'Color Picker',))
spinning = st.sidebar.selectbox('Set model spin', ('Off', 'On'))

if pdb and pdb in pdb_names_dict.all_pdbs_dict.values():
    url1 = f'https://files.rcsb.org/download/{pdb}.pdb1.gz'
    file_name1 = re.split(pattern='/', string=url1)[-1]
    r1 = request.urlopen(url=url1)

    with gzip.open(r1, 'rt') as f_in:
        bio_assembly = f_in.readlines()
        parsed_pdb = ''
        for line in bio_assembly:
            if line.startswith('ATOM'):
                parsed_pdb += line

    view = py3Dmol.view(width=width, height=height)
    view.addModelsAsFrames(parsed_pdb)
    view.setStyle({'model': -1}, {'cartoon': {'color': 'spectrum'}})

    # display pdb element title
    st.markdown(f'**[{pdb.upper()}](https://www.rcsb.org/structure/{pdb.upper()}): {utils.get_name(pdb)}**')

    chains, sequence = utils.parse_pdb(bio_assembly)

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

    if spinning == 'On':
        spin_axis = st.sidebar.selectbox('Which axis?', ('x', 'y', 'z'))
        speed = st.sidebar.slider('How fast? (Default is 1)', min_value = 0.25, max_value=2., value=1., step=0.25)
        spin_reverse = st.sidebar.selectbox('Reverse?', ('False', 'True'))
        spin_direction = 1.0 if spin_reverse == 'False' else -1.0
        view.spin(spin_axis, speed * spin_direction)

    button = st.sidebar.button('Reset view', on_click=view.zoomTo)

    view.zoomTo()
    view.show()

    showmol(view, width=width, height=height)

    st.download_button('Download sequence as fasta', f'>{pdb}\n{sequence}\n', file_name=f'{pdb}.fasta')

# center the title
st.markdown('<style>.e16nr0p30 {text-align: center;}</style>', unsafe_allow_html=True)

# adjust the view size and add a border
st.markdown('<style>iframe {border: solid; display: block; margin-left: auto; margin-right: auto; padding-left: 0px;}</style>', unsafe_allow_html=True)
