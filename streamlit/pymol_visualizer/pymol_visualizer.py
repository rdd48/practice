import streamlit as st
import py3Dmol
from stmol import showmol

st.set_page_config(
    page_title='Pymol Visualizer',
    page_icon=':atom_symbol:',
    layout='wide'
)

st.markdown('#### :atom_symbol:  Pymol Visualizer  :atom_symbol:')
mobile_size = st.checkbox('Optimize for mobile?', value=False)

# how to use py3Dmol: https://william-dawson.github.io/using-py3dmol.html
# with open('1fsl.pdb') as pdb:
#     system = ''.join([i for i in pdb])

# globals
width = 250 if mobile_size else 600
height = 250 if mobile_size else 400

st.sidebar.header('Select options:')
pdb = st.sidebar.text_input('Enter PDB code:', value='1fsl')

color_selector = st.sidebar.selectbox('Select color from picker or from pymol defaults:', ('Spectrum', 'Color Picker', 'cbc'))
if color_selector == 'Color Picker':
    color = st.sidebar.color_picker('Select color from picker:', value='#00f900')
elif color_selector:
    color = color_selector.lower()

spinning = st.sidebar.selectbox('Set model spin', ('False', 'True'))

view = py3Dmol.view(query=f'pdb:{pdb.strip()}', width=width, height=height)
view.setStyle({'model': -1}, {'cartoon': {'color': color}})

if spinning == 'True':
    spin_axis = st.sidebar.selectbox('Which axis?', ('x', 'y', 'z'))
    speed = st.sidebar.slider('How fast? (Default is 1)', min_value = 0.5, max_value=3., value=1., step=0.5)
    spin_reverse = st.sidebar.selectbox('Reverse?', ('False', 'True'))
    spin_direction = 1.0 if spin_reverse == 'False' else -1.0
    view.spin(spin_axis, speed * spin_direction)
    # st.markdown(f'{speed}, {speed*spin_direction}, {spin_direction}')

button = st.sidebar.button('Reset view', on_click=view.zoomTo)

# center the title
st.markdown('<style>.e16nr0p30 {text-align: center;}</style>', unsafe_allow_html=True)

# adjust the view size and add a border
st.markdown('<style>iframe {border: solid; display: block; margin-left: auto; margin-right: auto;}</style>', unsafe_allow_html=True)

view.zoomTo()
view.show()


showmol(view, width=width, height=height)