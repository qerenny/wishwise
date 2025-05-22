from typing import Generic, TypeVar, Type, List, Callable
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from wishwise_pr.configs.database.engine import get_db_connection
from wishwise_pr.services.base_service import BaseService

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType")
UpdateSchemaType = TypeVar("UpdateSchemaType")
PublicSchemaType = TypeVar("PublicSchemaType")
ServiceType = TypeVar("ServiceType", bound=BaseService)


def create_crud_router(
    *,
    prefix: str,
    tags: List[str],
    service_class: Type[ServiceType],
    public_schema: Type[PublicSchemaType],
) -> APIRouter:
    router = APIRouter(prefix=prefix, tags=tags)

    def get_service(session: AsyncSession = Depends(get_db_connection)) -> ServiceType:
        return service_class(session)

    @router.get("/", response_model=List[public_schema])
    async def list_all(service: ServiceType = Depends(get_service)):
        return await service.list()

    @router.get("/{id}", response_model=public_schema)
    async def get_by_id(id: int, service: ServiceType = Depends(get_service)):
        return await service.get(id)

    @router.post("/", response_model=public_schema)
    async def create(
        body: Type[CreateSchemaType],
        service: ServiceType = Depends(get_service),
    ):
        return await service.create(body)

    @router.patch("/{id}", response_model=public_schema)
    async def update(
        id: int,
        body: Type[UpdateSchemaType],
        service: ServiceType = Depends(get_service),
    ):
        instance = await service.get(id)
        for key, value in body.dict(exclude_unset=True).items():
            setattr(instance, key, value)
        return await service.update(instance)

    @router.delete("/{id}")
    async def delete(id: int, service: ServiceType = Depends(get_service)):
        await service.delete(id)
        return {"message": "Deleted"}

    return router
