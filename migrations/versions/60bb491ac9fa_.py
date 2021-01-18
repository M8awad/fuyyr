
from alembic import op
import sqlalchemy as sa


#  Alembic.
revision = '60bb491ac9fa'
down_revision = '93726ed55607'
branch_labels = None
depends_on = None


def upgrade():
    # ### Migration >>>>> ###
    op.add_column('Venue', sa.Column('genres', sa.Text(), nullable=True))
    #  Migration #


def downgrade():
    #  Migration >>>>> #
    op.drop_column('Venue', 'genres')
    #  Migration #
