from openerp import models, fields


class LHVPaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    lhv_PRIVATE_KEY = fields.Char('Private Key', size=256, help='Path to Private Key')
    lhv_BANK_CERT = fields.Char('Bank Certificate', size=256, help='Path to Bank Certificate')

    def _get_providers(self, cr, uid, context=None):
        providers = super(LHVPaymentAcquirer, self)._get_providers(cr, uid, context=context)
        providers.append(['lhv', 'LHV'])
        return providers

    def lhv_form_generate_values(self, cr, uid, id, partner_values, tx_values, context=None):
        return self.banklink_form_generate_values(cr, uid, id, partner_values, tx_values, context=context)

    def lhv_get_private_key(self):
        return self.lhv_PRIVATE_KEY

    def lhv_get_bank_cert(self):
        return self.lhv_BANK_CERT

    def lhv_get_form_action_url(self, cr, uid, id, context=None):
        env = self.read(cr, uid, id, ['environment'], context=context)['environment']
        return env == 'prod' and 'https://www.lhv.ee/banklink' or 'http://localhost:3480/banklink/lhv-common'
