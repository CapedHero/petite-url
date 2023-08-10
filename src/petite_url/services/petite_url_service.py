from src.petite_url import domain_objects as domain
from src.petite_url import models
from src.petite_url.services.petite_code_service import create_petite_code


def create_petite_url(target_url: str) -> domain.PetiteURL:
    petite_code = create_petite_code()
    petite_url_model = models.PetiteURL.objects.create(
        target_url=target_url,
        petite_code=petite_code,
    )
    return _convert_petite_url_model_to_domain_obj(petite_url_model)


def get_petite_url(petite_code: str) -> domain.PetiteURL:
    petite_url_model = models.PetiteURL.objects.get(petite_code=petite_code)
    return _convert_petite_url_model_to_domain_obj(petite_url_model)


def _convert_petite_url_model_to_domain_obj(
    model: models.PetiteURL,
) -> domain.PetiteURL:
    return domain.PetiteURL(
        target_url=model.target_url,
        petite_code=model.petite_code,
        created_at=model.created_at,
    )
