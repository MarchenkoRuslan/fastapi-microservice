"""update client and profile models

Revision ID: xxx
Revises: previous_revision
Create Date: 2024-xx-xx

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("profiles", sa.Column("phone", sa.String(), nullable=True))
    op.add_column("profiles", sa.Column("region", sa.String(), nullable=True))
    op.add_column("profiles", sa.Column("city", sa.String(), nullable=True))
    op.add_column("profiles", sa.Column("full_name", sa.String(), nullable=True))
    op.add_column(
        "profiles", sa.Column("binance_seller_name", sa.String(), nullable=True)
    )
    op.add_column(
        "profiles", sa.Column("binance_seller_nickname", sa.String(), nullable=True)
    )
    op.add_column(
        "profiles", sa.Column("binance_seller_mobile_phone", sa.String(), nullable=True)
    )

    op.add_column("clients", sa.Column("binance_user_hash", sa.String(), nullable=True))
    op.create_index(
        op.f("ix_clients_binance_user_hash"),
        "clients",
        ["binance_user_hash"],
        unique=True,
    )

    # Удаляем старые колонки
    op.drop_column("clients", "binance_user_id")
    op.drop_column("clients", "name")
    op.drop_column("profiles", "first_name")
    op.drop_column("profiles", "last_name")
    op.drop_column("profiles", "birth_date")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_clients_binance_user_hash"), table_name="clients")
    op.drop_column("clients", "binance_user_hash")
    op.drop_column("profiles", "binance_seller_mobile_phone")
    op.drop_column("profiles", "binance_seller_nickname")
    op.drop_column("profiles", "binance_seller_name")
    op.drop_column("profiles", "full_name")
    op.drop_column("profiles", "city")
    op.drop_column("profiles", "region")
    op.drop_column("profiles", "phone")
    # ### end Alembic commands ###
