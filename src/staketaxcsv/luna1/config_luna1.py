from staketaxcsv.common import ExporterTypes as et
from staketaxcsv.common.config import config


class localconfig(config):

    minor_rewards = False
    # Treat LP deposits/withdrawals as "transfers"/"omit"/"trades" (ignored for koinly)
    lp_treatment = et.LP_TREATMENT_DEFAULT

    # caches
    ibc_addresses = {}
    # <currency_address> -> <currency_symbol>
    currency_addresses = {
        'terra1t9ul45l7m6jw6sxgvnp8e5hj8xzkjsg82g84ap': 'wstSOL',
    }
    decimals = {}  # <currency_symbol> -> <number_of_decimals>
    lp_currency_addresses = {}  # <lp_currency_address> -> <lp_currency_symbol>
