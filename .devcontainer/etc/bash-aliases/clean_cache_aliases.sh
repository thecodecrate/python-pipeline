alias rm_pycache='find . -name "__pycache__" | xargs rm -rf;'
alias rm_egginfo='find . -name "*.egg-info"  | xargs rm -rf;'
alias rm_dist='find . -name "dist"  | xargs rm -rf;'
alias clean='rm_pycache; rm_egginfo; rm_dist'
