"""empty message

Revision ID: c8f23f7a9834
Revises: 730ba711f62c
Create Date: 2025-04-02 12:33:40.321154

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c8f23f7a9834'
down_revision = '730ba711f62c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roles_users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('roles_users_role_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('roles_users_staff_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'roles', ['role_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])
        batch_op.drop_column('staff_id')

    with op.batch_alter_table('staffs', schema=None) as batch_op:
        batch_op.drop_constraint('staffs_fs_uniquifier_key', type_='unique')
        batch_op.drop_column('fs_uniquifier')
        batch_op.drop_column('password')
        batch_op.drop_column('active')
        batch_op.drop_column('username')
        batch_op.drop_column('last_login')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('staffs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_login', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('active', sa.BOOLEAN(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('fs_uniquifier', sa.VARCHAR(length=150), autoincrement=False, nullable=False))
        batch_op.create_unique_constraint('staffs_fs_uniquifier_key', ['fs_uniquifier'])

    with op.batch_alter_table('roles_users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('staff_id', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('roles_users_staff_id_fkey', 'staffs', ['staff_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('roles_users_role_id_fkey', 'roles', ['role_id'], ['id'], ondelete='CASCADE')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
