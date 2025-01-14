# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Add METADATA digest column to Release Files

Revision ID: 2b2f58288de1
Revises: fd0479fed881
Create Date: 2023-05-11 14:25:53.582849
"""

import citext
import sqlalchemy as sa

from alembic import op

revision = "2b2f58288de1"
down_revision = "fd0479fed881"


def upgrade():
    op.add_column(
        "release_files",
        sa.Column("metadata_file_sha256_digest", citext.CIText(), nullable=True),
    )
    op.add_column(
        "release_files",
        sa.Column("metadata_file_blake2_256_digest", citext.CIText(), nullable=True),
    )


def downgrade():
    op.drop_column("release_files", "metadata_file_blake2_256_digest")
    op.drop_column("release_files", "metadata_file_sha256_digest")
