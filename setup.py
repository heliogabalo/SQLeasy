from distutils.core import setup

setup(
  name = 'SQLeasy',
  packages = ['SQLeasy'],
  version = '1.0.0',
  description = 'Automate sql queries',
  author = 'Raul Vilchez',
  url = "",
  download_url = "",
  keywords = ["Automation", "Databases", "SAME, Small And Medium Enterprises"],
  classifiers = [
  'Programmin Language :: Python',
  'Programmin Language :: Python :: 3',
  'Programmin Language :: PL/SQL',
  'License :: OSI Approved :: GNU Library or General Public License(GPL)'
  'operating System :: OS Independent',
  'Development Status :: 3 - Alpha',
  'Environment :: Other Environment',
  'FrameWork :: Sphinx',
  'FrameWork :: IPython',
  'Intended Audience :: Developers',
  'Topic :: Home Automation',
  'Topic :: Utilities'
  ],
  long_description = """\
  SAME sqlIzer 4 all
  ------------------

  Appliance:
  - Test DataBases Server connection
  - Create, delete, display DataBases
  - Create, delete, modify and display DataBases tables
  - Automate data insertion
  - Transform sql data structures into re-usable html code.

  This version requires Python 3 or later; a Python 2 version it's available
  under explicit demand.
  """
)
