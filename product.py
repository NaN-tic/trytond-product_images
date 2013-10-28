#The COPYRIGHT file at the top level of this repository contains the full
#copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Eval

__all__ = ['Attachment', 'Template']
__metaclass__ = PoolMeta


class Attachment:
    __name__ = 'ir.attachment'

    product_image = fields.Boolean('Product Image')


class Template:
    __name__ = 'product.template'

    images = fields.One2Many('ir.attachment', 'resource', 'Images', domain=[
            ('product_image', '=', True),
            ],
        context={
            'resource': Eval('id'),
            }, depends=['id'])

    @classmethod
    def delete(cls, templates):
        pool = Pool()
        Attachment = pool.get('ir.attachment')

        attachments = [a for t in templates for a in t.images]
        Attachment.delete(attachments)
        super(Template, cls).delete(templates)
