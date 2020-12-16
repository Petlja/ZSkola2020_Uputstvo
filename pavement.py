import paver
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()
import os, sys
from runestone.server import get_dburl
from sphinxcontrib import paverutils
import pkg_resources

sys.path.append(os.getcwd())

home_dir = os.getcwd()
master_url = 'http://127.0.0.1:8000'
master_app = 'runestone'
serving_dir = "./build/ZSkola2020_Uputstvo"
dest = "docs"

options(
    sphinx = Bunch(docroot=".",),

    build = Bunch(
        builddir="./build/ZSkola2020_Uputstvo",
        sourcedir="_sources",
        outdir="./build/ZSkola2020_Uputstvo",
        confdir=".",
        project_name = "ZSkola2020_Uputstvo",
        template_args={'course_id': 'ZSkola2020_Uputstvo',
                       'login_required':'false',
                       'appname':master_app,
                       'loglevel': 0,
                       'course_url':master_url,
                       'use_services': 'false',
                       'python3': 'true',
                       'dburl': '',
                       'default_ac_lang': 'python',
                       'basecourse': 'ZSkola2020_Uputstvo',
                       'jobe_server': 'http://jobe2.cosc.canterbury.ac.nz',
                       'proxy_uri_runs': '/jobe/index.php/restapi/runs/',
                       'proxy_uri_files': '/jobe/index.php/restapi/files/',
                       'downloads_enabled': 'false',
                       'enable_chatcodes': 'false'
                        }
    )
)

# If DBURL is in the environment override dburl
options.build.template_args['dburl'] = get_dburl(outer=locals())

from runestone import build  # build is called implicitly by the paver driver.
