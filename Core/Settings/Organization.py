# Import modules

import os


# Organizations list (By Directories)

OrganizationsPaths = (
    'C:\\Users\\John\\Desktop\\foobar.txt',
    'C:\\Users\\Peter Wilson\\Desktop\\Microsoft Word 2010.lnk',
    'C:\\Users\\Lisa\\Desktop',
    'C:\\Users\\Administrator\\Desktop\\decoy.cpp',
    'C:\\Users\\Jason\\Desktop')


# Detect Antivirus organization by Directories

def Organization():
    return any([os.path.exists(Organization) for Organization in OrganizationsPaths])
