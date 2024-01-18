import datetime

from src.config.settings import SupplierWebSettings
from src.services.states.states import SupplierClienState

from ._common import get_state_body_fields


def get_leftover_form_body(state: SupplierClienState) -> dict:
    body = dict.fromkeys(SupplierWebSettings.LEFTOVERS_FORM_FIELDS)

    body.update(
        get_state_body_fields(state=state) | _get_leftovers_form_fields()
    )

    return body


def _get_leftovers_form_fields() -> dict:
    return {
        SupplierWebSettings.PL_FIELD_NAME: SupplierWebSettings.PL,
        SupplierWebSettings.SKLAD_ID_FIELD_NAME: SupplierWebSettings.SKLAD_ID,
        SupplierWebSettings.REPORT_DATE_FIELD_NAME: _get_today(),
        SupplierWebSettings.REPORT_FORMAT_FIELD_NAME: SupplierWebSettings.REPORT_FORMAT
    }


def _get_today() -> str:
    return datetime.datetime.today(
        ).strftime(
        format=SupplierWebSettings.DATE_FORMAT
    )
