import odoorpc

# Prepare the connection to the server
odoo = odoorpc.ODOO('localhost', port=8069)


# Login
odoo.login('dzitodoo', 'admin', 'admin')

# Current user
if 'product.template' in odoo.env:
	#this returns a lot of id's
	product_ids = odoo.env['product.template'].search([])
	call_my_dzit_product=odoo.env['product.template'].browse(29)
	call_my_dzit_product.barcode="355367HH3GGEUSGTARR63637YE"
