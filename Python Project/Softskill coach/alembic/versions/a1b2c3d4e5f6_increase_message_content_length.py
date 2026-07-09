"""Increase message content length for AI replies

Revision ID: a1b2c3d4e5f6
Revises: 731d86fb796a
Create Date: 2026-07-09 23:55:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'a1b2c3d4e5f6'
down_revision: Union[str, Sequence[str], None] = '731d86fb796a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        'messages',
        'content',
        existing_type=sa.String(length=500),
        type_=sa.Text(),
        existing_nullable=False
    )


def downgrade() -> None:
    op.alter_column(
        'messages',
        'content',
        existing_type=sa.Text(),
        type_=sa.String(length=500),
        existing_nullable=False
    )
