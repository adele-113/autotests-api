from pydantic import BaseModel, Field, ConfigDict
from tools.fakers import fake

class ExerciseSchema(BaseModel):
    """
    Описание структуры упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)
    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    model_config = ConfigDict(populate_by_name=True)
    course_id: str = Field(alias="courseId")

class GetExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на получение упражнения.
    """
    exercise_id: str

class GetExerciseResponseSchema(BaseModel):
    """
        Описание структуры ответа на получение упражнения.
        """
    model_config = ConfigDict(populate_by_name=True)
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class CreateExercisesRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)
    title: str = Field(default_factory=fake.sentence)
    courseId: str = Field(default_factory=fake.uuid4)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)

class CreateExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа создания упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)
    exercise: ExerciseSchema

class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа списка упражнений.
    """
    model_config = ConfigDict(populate_by_name=True)
    exercises: list[ExerciseSchema]

class UpdateExercisesRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)
    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int | None = Field(alias="orderIndex", default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str| None  = Field(alias="estimatedTime", default_factory=fake.estimated_time)

class UpdateExercisesResponseSchema(BaseModel):
    """
        Описание структуры ответа обновления упражнения.
        """
    model_config = ConfigDict(populate_by_name=True)
    exercise: ExerciseSchema