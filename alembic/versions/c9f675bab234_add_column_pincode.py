"""add column pincode

Revision ID: c9f675bab234
Revises: 
Create Date: 2024-07-16 20:43:03.005225

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'c9f675bab234'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('crickter', sa.Column('starting_year', sa.String(30)))


def downgrade() -> None:
    op.drop_column('crickter', 'starting_year')
