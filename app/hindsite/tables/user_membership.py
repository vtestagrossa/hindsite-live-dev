"""
Association table for groups and users.
"""
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.hindsite import db


class UserMembership(db.Model):
    """
    Associates user and groups.
    """
    __tablename__ = 'user_membership'

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), primary_key=True)
    group_id: Mapped[int] = mapped_column(ForeignKey('hindsite_group.id'), primary_key=True)
    user: Mapped['User'] = relationship(back_populates='groups')
    group: Mapped['Group'] = relationship(back_populates='users')
    owner: Mapped[bool] = mapped_column(default=False)
    invitation_accepted: Mapped[bool] = mapped_column(default=False)
