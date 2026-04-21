"""check_new_template

Revision ID: 2145e850812a
Revises: d0cc910ec850
Create Date: 2026-04-21 18:11:10.586043

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2145e850812a'
down_revision: Union[str, Sequence[str], None] = 'd0cc910ec850'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
