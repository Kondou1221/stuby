from pydantic import BaseModel
import datetime

#リプライベーススキーマ, 新規のリプライのリクエストスキーマ
class base_comment_schma(BaseModel):
    user_id: int
    post_id: int
    comment_sentence: str = None
    mention_id: int = None

#いいねの追加と削除のリクエストスキーマ
class commentgood_request(BaseModel):
    comment_id: int
    user_id: int

#リプライのレスポンススキーマ
class select_comment_id(base_comment_schma):
    comment_id: int
    user_name: str
    comment_create: datetime.datetime

    class Config():
        orm_mode = True