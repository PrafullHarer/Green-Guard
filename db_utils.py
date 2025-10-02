from typing import Any, Dict, Optional


class InMemoryDB:
    def __init__(self) -> None:
        self.users: Dict[str, Dict[str, Any]] = {}
        self.users_by_email: Dict[str, str] = {}
        self.disease_records: list[Dict[str, Any]] = []
        self._id_counter = 1

    def _new_id(self) -> str:
        new_id = str(self._id_counter)
        self._id_counter += 1
        return new_id

    # Users
    def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        user_id = self.users_by_email.get(email)
        if not user_id:
            return None
        return self.users.get(user_id)

    def create_user(self, user_data: Dict[str, Any]) -> Optional[str]:
        if user_data.get("email") in self.users_by_email:
            return None
        user_id = self._new_id()
        record = {"_id": user_id, **user_data}
        self.users[user_id] = record
        self.users_by_email[user_data["email"]] = user_id
        return user_id

    def get_user(self, user_id: str) -> Optional[Dict[str, Any]]:
        return self.users.get(user_id)

    # Disease records
    def save_disease_record(self, user_id: str, filename: str, prediction: str) -> None:
        self.disease_records.append(
            {"user_id": user_id, "filename": filename, "prediction": prediction}
        )


# Simple module-level instance to match expected import usage
db = InMemoryDB()

