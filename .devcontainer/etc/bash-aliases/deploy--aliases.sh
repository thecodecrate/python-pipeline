# Alias for publishing the package to pypi
alias _clean_dist='find . -type d -name "dist" -exec rm -rf {} +'
alias bump='bumpver update --minor'
alias build='_clean_dist; uv build'
alias deploy='uv publish'
