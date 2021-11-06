if [ ! -f app/config/service_account.json ];
  then echo "Service account file not present";
  exit 1;
fi
npm install -g @angular/cli
cd angular-client && npm install
cd ..
npm run clientbuild