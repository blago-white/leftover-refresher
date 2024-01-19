from src.config.settings import SupplierSettings
from src.services.states.states import SupplierClienState


def get_state_body_fields(state: SupplierClienState) -> dict:
    return {
        SupplierSettings.VIEWSTATE_FIELD_NAME: state.viewstate,
        SupplierSettings.GENERATOR_FIELD_NAME: state.generator,
        SupplierSettings.EVENTVALIDATION_FIELD_NAME: state.eventvalidation
    }
