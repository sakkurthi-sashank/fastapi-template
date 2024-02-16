"""create users table

Revision ID: e5bb40ba6bb1
Revises:
Create Date: 2024-02-15 23:30:12.037619

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e5bb40ba6bb1"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column(
            "id",
            sa.UUID(as_uuid=True),
            server_default=sa.text("gen_random_uuid()"),
            primary_key=True,
            unique=True,
            nullable=False,
        ),
        sa.Column("display_name", sa.String(255)),
        sa.Column("email", sa.String(255), unique=True, nullable=False, index=True),
        sa.Column("photo_url", sa.String(255), nullable=True),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            onupdate=sa.text("now()"),
        ),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
        ),
    )


def downgrade() -> None:
    op.drop_table("users")
