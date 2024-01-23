from fastapi import APIRouter

APIRouter.enter = lambda self: self
APIRouter.exit = lambda *args: ''

router = APIRouter(prefix='/app',
                   tags=['app'])

users = APIRouter(prefix='/users',
                      tags=['users'])

ads_bs = APIRouter(prefix='/ads_bs',
                      tags=['ads_bs'])

ads_rent = APIRouter(prefix='/ads_rent',
                        tags=['ads_rent'])

auth = APIRouter(prefix='/auth',
                 tags=['auth'])

logs = APIRouter(prefix='/logs',
                 tags=['logs'])

for_admins = APIRouter(prefix='/admin',
                       tags=['for_admins'])


# здесь указываем эндпоинты
router.get("")(FrontMainController.index)
router.get("/auth")(FrontMainController.user_auth)
router.get("/ping")(FrontMainController.ping)

ads_bs.post("/generate_list")(FrontMainController.generate_list)
ads_bs.post("/invoice")(FrontMainController.generate_invoice)

ads_rent.post("/create")(GeoLocationController.create)
ads_rent.post("/get-by-id")(GeoLocationController.get_by_id)

auth.post("/token")(AuthController.token)
auth.post("/create_new_user")(AuthController.create_new_user)

logs.get("/get_all")(LogsController.logs)

for_admins.delete("/delete_emails")(AdminController.remove_emails)
for_admins.post("/create_email")(AdminController.create_email)