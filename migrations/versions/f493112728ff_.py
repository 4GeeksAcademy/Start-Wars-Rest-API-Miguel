"""empty message

Revision ID: f493112728ff
Revises: a5cffa318ac2
Create Date: 2025-02-19 16:21:47.451451

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f493112728ff'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('birth_year', sa.String(length=10), nullable=False),
    sa.Column('eye_color', sa.String(length=10), nullable=False),
    sa.Column('gender', sa.String(length=10), nullable=False),
    sa.Column('hair_color', sa.String(length=10), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('homeworld', sa.String(length=200), nullable=False),
    sa.Column('mass', sa.Integer(), nullable=False),
    sa.Column('skin_color', sa.String(length=30), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('edited', sa.DateTime(), nullable=False),
    sa.Column('species', sa.String(length=200), nullable=False),
    sa.Column('starships', sa.String(length=200), nullable=False),
    sa.Column('url', sa.String(length=200), nullable=False),
    sa.Column('vehicles', sa.String(length=200), nullable=False),
    sa.Column('films', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planet',
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('climate', sa.String(length=10), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('diameter', sa.Integer(), nullable=False),
    sa.Column('edited', sa.DateTime(), nullable=False),
    sa.Column('films', sa.String(length=200), nullable=False),
    sa.Column('gravity', sa.Integer(), nullable=False),
    sa.Column('orbital_period', sa.Integer(), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('residents', sa.String(length=200), nullable=False),
    sa.Column('rotation_period', sa.Integer(), nullable=False),
    sa.Column('surface_water', sa.Integer(), nullable=False),
    sa.Column('terrain', sa.String(length=20), nullable=False),
    sa.Column('url', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicle',
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cargo_capacity', sa.Integer(), nullable=False),
    sa.Column('consumables', sa.String(length=20), nullable=False),
    sa.Column('cost_in_credits', sa.Float(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('crew', sa.Integer(), nullable=False),
    sa.Column('edited', sa.DateTime(), nullable=False),
    sa.Column('length', sa.Float(), nullable=False),
    sa.Column('manufacturer', sa.String(length=40), nullable=False),
    sa.Column('max_atmosphering_speed', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=30), nullable=False),
    sa.Column('passengers', sa.Integer(), nullable=False),
    sa.Column('pilots', sa.String(length=100), nullable=False),
    sa.Column('films', sa.String(length=200), nullable=False),
    sa.Column('url', sa.String(length=200), nullable=False),
    sa.Column('vehicle_class', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicle')
    op.drop_table('planet')
    op.drop_table('character')
    # ### end Alembic commands ###
