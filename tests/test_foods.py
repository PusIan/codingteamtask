import pytest
from rest_framework import status


class TestFoodsApi:
    ENDPOINT = '/api/v1/foods/'

    @pytest.mark.django_db(transaction=True)
    def test_get_foods_success(self, client, food_category1, food_category2,
                               food1, food2, food3):
        response = client.get(self.ENDPOINT)
        assert response.status_code != status.HTTP_404_NOT_FOUND, (
            f'Страница `{self.ENDPOINT}` не найдена, ',
            'проверьте этот адрес в *urls.py*')
        assert response.status_code == status.HTTP_200_OK, (
            f'Проверьте, что `{self.ENDPOINT}` при запросе ',
            f'без токена возвращаете статус {status.HTTP_200_OK}')
