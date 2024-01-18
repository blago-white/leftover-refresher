from src.config.settings import SupplierWebSettings
from src.services.states.states import SupplierClienState


def get_state_body_fields(state: SupplierClienState) -> dict:
    return {
        SupplierWebSettings.VIEWSTATE_FIELD_NAME: state.viewstate,
        SupplierWebSettings.GENERATOR_FIELD_NAME: state.generator,
        SupplierWebSettings.EVENTVALIDATION_FIELD_NAME: state.eventvalidation
    }
