import warnings
import sys

warnings.warn(
    "\nYou have installed 'any-agents' (with an 's'), but you probably meant to install 'any-agent'.\n"
    "The correct package 'any-agent' has been automatically installed as a dependency.\n"
    "Please use 'any-agent' in your imports to avoid confusion.",
    UserWarning,
    stacklevel=2
)