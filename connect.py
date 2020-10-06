# import Libs
from prestapyt import *
import odoorpc



# Prepare the connection to the server
odoo = odoorpc.ODOO('localhost', port=8069)


# Login credentials to the odoo API
odoo.login('dzitodoo', 'admin', 'admin')


#connecting to the prestashop WS rest API
prestashop = PrestaShopWebServiceDict("http://localhost:8080/api", "XK314MB2NT7IJJJN6XKIWPZWS1E6IXBR")

#retrieving the product we wanna do some operation on (static retrieving for demonstration purposes)
pro=prestashop.get("products",32)



product_name_in_prestashop=pro['product']['name']['language'][0]['value']
product_price_in_prestashop=pro['product']['price']



# Current user
if 'product.template' in odoo.env:
	#this returns a lot of id's
	product_ids = odoo.env['product.template'].search([])
	call_my_dzit_product=odoo.env['product.template'].browse(29)
	call_my_dzit_product.name=product_name_in_prestashop
	call_my_dzit_product.list_price=product_price_in_prestashop










