###################################################################################
# 
#    Copyright (C) 2017 Mediproyect S.A.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

{
    "name": "Customer Age, Last Payment and Last Invoice",
    "summary": """Adds support for Customer Age, Birthday, Last Payment (date and amount) and Last Invoice (date and amount)""",
    "version": "1.0",
    "category": "Extra Tools",
    "license": "AGPL-3",
    "website": "https://medic.site",
    "author": "Mediproyect S.A.",
    "contributors": [
        "Carlos Marrero <cdmarrero2040@gmail.com>",
    ],
    "depends": [
        "account",
        "base_setup",
        "contacts",
    ],
    "data": [
        "views/res_partner_view.xml",
    ],
    "images": [
        'static/description/thumbnails.png'
    ],
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "application": False,
    "installable": True,
    "auto_install": False,
}