import active as active
import odoorpc
from prestapyt import PrestaShopWebService
from xml.etree import ElementTree

# Prepare the connection to the server
from prestapyt import PrestaShopWebServiceDict

odoo = odoorpc.ODOO('localhost', port=8069)


# Login
odoo.login('dzitodoo', 'admin', 'admin')




# import Libs
from prestapyt import *
#--------------------------------------------------------------------------------------------------------------------

prestashop = PrestaShopWebServiceDict("http://localhost:8080/api", "XK314MB2NT7IJJJN6XKIWPZWS1E6IXBR")

pro=prestashop.get("products",32)

product_name_in_prestashop=pro['product']['name']['language'][0]['value']




# Current user
if 'product.template' in odoo.env:
	#this returns a lot of id's
	product_ids = odoo.env['product.template'].search([])
	call_my_dzit_product=odoo.env['product.template'].browse(29)
	call_my_dzit_product.name=product_name_in_prestashop











