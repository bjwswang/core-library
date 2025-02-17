# Copyright 2024 KubeAGI.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from pathlib import Path
from typing import List

from kubeagi_core.document_loaders.base import BaseLoader
from langchain.document_loaders import Docx2txtLoader

logger = logging.getLogger(__name__)


class DocxLoader(BaseLoader):
    """Load docx files."""

    def __init__(
        self,
        file_path: str,
    ):
        """
        Initialize the loader with a list of URL paths.

        Args:
            file_path (str): File Path.
        """
        self._file_path = file_path

    def load(self) -> List:
        """
        Load and return all Documents from the docx file.

        Returns:
            List: A list of Document objects.

        """
        logger.info("Start to load docx file")

        # Get file name
        path = Path(self._file_path)
        file_name = path.name

        docx_loader = Docx2txtLoader(self._file_path)
        documents = docx_loader.load()
        for document in documents:
            document.metadata["source"] = file_name

        return documents
