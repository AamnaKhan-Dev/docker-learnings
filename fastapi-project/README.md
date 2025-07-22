
# 🧠 FastAPI + Pydantic | Learning Notes

### 📌 Objective
Explore how FastAPI + Pydantic enables **data validation**, **normalization**, and **clean structuring** in API requests.

---

## ✅ Key Learnings

### 📦 Pydantic Basics
- `BaseModel` is used to define data schemas.
- Use `Field(..., gt=, lt=)` for constraints.
- Optional fields: `Optional[type] = None`.

### 📍 Nested Models
```python
class Contact(BaseModel):
    phNo: str
    address: str
    email: EmailStr
````

### 🧹 Data Cleaning

* `.title()` for name formatting.
* `.strip()` to remove extra spaces.
* Email lowercased + validated against custom domain list.

### ☎️ Phone Number Normalization

* Accepts formats like `0308-333-1698`, `+92...`, etc.
* Output: `+92308XXXXXXX`.

---

## 🧪 Sample Payload

```json
{
  "name": "aamna khan",
  "age": 48,
  "allergies": ["pollen"],
  "contact_details": {
    "phNo": " 0308--333-1698",
    "address": "xyz",
    "email": "Aamna@NUST.edu.pk"
  }
}
```

### 🔍 After Processing

* `name`: `"Aamna Khan"`
* `email`: `"aamna@nust.edu.pk"`
* `phNo`: `+923175813294`

---

## 🧰 Tools Used

* **FastAPI** — for structuring API logic
* **Pydantic** — for robust validation
* **Python 3.10+**

---

## 🚧 Next Steps

* Add route endpoints (`@app.post(...)`)
* Create full CRUD logic
* Dockerize the app
* Build tests using `pytest`

---


