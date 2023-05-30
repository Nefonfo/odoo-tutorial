from odoo import fields, models
from dateutil import relativedelta

class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Model to save offers of Properties"

    price = fields.Float()
    status = fields.Selection(
        string="Status",
        selection=[('A', 'Accepted'), ('R', 'Refused')],
        help="Please select the status")
    partner_id = fields.Many2one("res.partner", string = "Partner", required = True)
    property_id = fields.Many2one("estate.property", string="Property", required = True)

class PropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Model for tags of Properties"

    name = fields.Char(required = True)

class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Model for types of Properties"

    name = fields.Char(required = True)

class Property(models.Model):
    _name = "estate.property"
    _description = "Model for Properties"

    name = fields.Char(required = True, default = 'Unknown')
    description = fields.Text()
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    salesman_id = fields.Many2one("res.users", string="Salesman", readonly = True, default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    property_type_id = fields.Many2one("estate.property.type", string = "Property Type")
    post_code = fields.Char()
    date_availability = fields.Date(default = fields.Date().today() + relativedelta.relativedelta(months=3))
    expected_price = fields.Float(required = True)
    selling_price = fields.Float(readonly = True, copy = False)
    bedrooms = fields.Integer(default = 3)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Type',
        selection=[('N', 'North'), ('S', 'South'), ('E', 'East'), ('W', 'West')],
        help='Please select the orientation')
    active = fields.Boolean()
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")