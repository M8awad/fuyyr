
from alembic import op
import sqlalchemy as sa


# Alembic 
revision = '2592c670e7b4'
down_revision = '60bb491ac9fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### Migration >>>>> ###
    op.alter_column('Artist', 'genres',
                    existing_type=sa.VARCHAR(length=120),
                     nullable=False)
    op.alter_column('Venue', 'genres',
                    existing_type=sa.TEXT(),
                    nullable=False)
    #  Migration  #


def downgrade():
    # ### Migration >>>>> #
    op.alter_column('Venue', 'genres',
                    existing_type=sa.TEXT(),
                    nullable=True)
    op.alter_column('Artist', 'genres',
                    existing_type=sa.VARCHAR(length=120),
                    nullable=True)
    # ### Migration Result  ###
