
from alembic import op
import sqlalchemy as sa


# alembic##.
revision = '93726ed55607'
down_revision = 'ddbac8413238'
branch_labels = None
depends_on = None


def upgrade():
    # ### Migration >>>>> ###
    op.create_table('shows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('upcoming', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('Artist', sa.Column('past_shows_count', sa.Integer(), nullable=True))
    op.add_column('Artist', sa.Column('seeking_description', sa.Text(), nullable=True))
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.add_column('Artist', sa.Column('upcoming_shows_count', sa.Integer(), nullable=True))
    op.add_column('Artist', sa.Column('website', sa.String(length=120), nullable=True))
    op.add_column('Venue', sa.Column('past_shows_count', sa.Integer(), nullable=True))
    op.add_column('Venue', sa.Column('seeking_description', sa.Text(), nullable=True))
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('Venue', sa.Column('upcoming_shows_count', sa.Integer(), nullable=True))
    op.add_column('Venue', sa.Column('website', sa.String(length=120), nullable=True))
    # ### Migration Result  ###


def downgrade():
    # ### Migration >>>>> ###
    op.drop_column('Venue', 'website')
    op.drop_column('Venue', 'upcoming_shows_count')
    op.drop_column('Venue', 'seeking_talent')
    op.drop_column('Venue', 'seeking_description')
    op.drop_column('Venue', 'past_shows_count')
    op.drop_column('Artist', 'website')
    op.drop_column('Artist', 'upcoming_shows_count')
    op.drop_column('Artist', 'seeking_venue')
    op.drop_column('Artist', 'seeking_description')
    op.drop_column('Artist', 'past_shows_count')
    op.drop_table('shows')
    # ### Migration Result  ###
