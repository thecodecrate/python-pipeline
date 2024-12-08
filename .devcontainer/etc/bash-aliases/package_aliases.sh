# Alias for publishing the package to pypi
alias clean_dist='find . -name "dist"  | xargs rm -rf;'
alias bump='bumpver update --minor'
alias build='clean_dist; uv build'
alias deploy='uv publish'
