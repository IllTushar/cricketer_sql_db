"""add column avg_rate

Revision ID: 28482e07fde8
Revises: c9f675bab234
Create Date: 2024-07-16 21:54:22.736225

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '28482e07fde8'
down_revision: Union[str, None] = 'c9f675bab234'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


# You can delete only those column which you add by alembic

def upgrade() -> None:
    op.add_column("strike_rate", sa.Column("avg_rate", sa.Integer))


def downgrade() -> None:
    op.drop_column("strike_rate", "avg_rate")
