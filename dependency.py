# from fastapi import HTTPException, Depends
# from blog.oauth2 import get_current_user

# def admin_required(allowed_roles: list):
#     def wrapper(current_user: dict = Depends(get_current_user)):
#         if current_user.role not in allowed_roles:
#             raise HTTPException(
#                 status_code=403,
#                 detail="Not Permission. Admins only."
#             )
#         return current_user
#     return wrapper
