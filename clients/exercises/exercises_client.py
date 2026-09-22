from httpx import Response
from clients.exercises.exercises_schema import ExerciseSchema, GetExercisesQuerySchema, CreateExercisesRequestSchema, \
    UpdateExercisesRequestSchema, CreateExercisesResponseSchema, GetExercisesResponseSchema, GetExerciseRequestSchema, \
    UpdateExercisesResponseSchema
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод получения списка упражнений курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упраженения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExercisesRequestSchema) -> Response:
        """
        Метод создания упражнения.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercise_api(self, exercise_id: str, request: UpdateExercisesRequestSchema) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def create_exercise(self, request: CreateExercisesRequestSchema) -> CreateExercisesResponseSchema:
        response =  self.create_exercise_api(request)
        return CreateExercisesResponseSchema.model_validate_json(response.text)

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self, request: GetExerciseRequestSchema) -> GetExercisesResponseSchema:
        response = self.get_exercise_api(request)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def update_exercise(
            self,
            request: GetExerciseRequestSchema,
            update_request: UpdateExercisesRequestSchema
    ) -> UpdateExercisesResponseSchema:
        response = self.update_exercise_api(request["id"], update_request)
        return UpdateExercisesResponseSchema.model_validate_json(response.text)

def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.
    """
    return ExercisesClient(client=get_private_http_client(user))