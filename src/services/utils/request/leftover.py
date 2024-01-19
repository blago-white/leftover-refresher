import datetime

from src.config.settings import SupplierSettings
from src.services.states.states import SupplierClienState
from ._common import get_state_body_fields


def get_leftover_form_body(state: SupplierClienState) -> dict:
    body = dict.fromkeys(SupplierSettings.LEFTOVERS_FORM_FIELDS)

    body.update(
        get_state_body_fields(state=state) | _get_leftovers_form_fields()
    )

    return body


def _get_leftovers_form_fields() -> dict:
    return {
        SupplierSettings.PL_FIELD_NAME: SupplierSettings.PL,
        SupplierSettings.SKLAD_ID_FIELD_NAME: SupplierSettings.SKLAD_ID,
        SupplierSettings.REPORT_DATE_FIELD_NAME: _get_today(),
        SupplierSettings.REPORT_FORMAT_FIELD_NAME: SupplierSettings.REPORT_FORMAT
    }


def _get_today() -> str:
    return datetime.datetime.today(
        ).strftime(
        format=SupplierSettings.DATE_FORMAT
    )
