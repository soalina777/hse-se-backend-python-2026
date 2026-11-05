from models.comment import Comment
from models.user import User


def filter_comments_by_author(
    comments: list[Comment], author: User
) -> list[Comment]:
    result = []

    for comment in comments:
        if comment.author_id == author.id:
            result.append(comment)

    return result
