from src.config.config import SupplierCredentals
from src.config.settings import SupplierSettings
from src.services.states.states import SupplierClienState

from ._common import get_state_body_fields


def get_login_body(
        state: SupplierClienState,
        credentals: SupplierCredentals) -> dict:
    body = dict.fromkeys(SupplierSettings.LOGIN_FORM_FIELDS)

    body.update(
        get_state_body_fields(state=state) | _get_login_credentals_body_fields(
            credentals=credentals)
    )

    return body


def _get_login_credentals_body_fields(credentals: SupplierCredentals) -> dict:
    return {
        SupplierSettings.USERNAME_FIELD_NAME: credentals.username,
        SupplierSettings.PASSWORD_FIELD_NAME: credentals.password
    }
