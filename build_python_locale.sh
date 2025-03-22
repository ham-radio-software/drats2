#!/bin/bash

set -uex

base_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"

locale_base_dir="${base_dir}/drats_common/src/drats_common/locale"

# At this time not setting the details for the POT file.
domain='drats'
pybabel extract -o "${base_dir}/${domain}.pot" --input-dirs="${base_dir}" \
  --ignore-dir '*_env' \
  --project='D-Rats' \
  --copyright-holder='See COPYING file'

my_locals=('de' 'en' 'es' 'it' 'nl')
for locale in "${my_locals[@]}"; do
    action="update"
    lang_dir="${locale_base_dir}/${locale}/LC_MESSAGES/"
    if [ ! -e "${lang_dir}/${domain}.po" ]; then
        action="init"
    fi
    echo "Doing $action on ${locale_base_dir}"
    pybabel "$action" -i "${base_dir}/${domain}.pot" \
            -D "${domain}"                       \
            -l "${locale}"                       \
            -d "${locale_base_dir}"
done
pybabel compile -D "${domain}" \
            -d "${locale_base_dir}"