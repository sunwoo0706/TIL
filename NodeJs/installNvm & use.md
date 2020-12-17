# 버전 관리

[Node.js](./installNode.md)의 새로운 버전이 나올경우 버전을 업그레이드를 해야 하고, 하위 호환성을 위해서 버전을 다운그레이드를 해야 할 수 있습니다.

다양한 경우에 의해 버전의 변경이 자주 발생하므로 Node.js를 설치할 떄부터 버전 관리가 가능한 형태로 설치하는 것이 좋습니다.

Node.js의 버전 관리를 위한 대표적인 관리 매니저로 [NVM](https://github.com/nvm-sh/nvm)과 [n](https://github.com/tj/n)이 있습니다.<br />
NVM과 n은 서로 유사한 기능을 제공합니다.<br />
<small>[ 단 윈도우에서는 안깔린답니당 ^^ 대체재가 있긴하지만요 (nvm-window, nodist)]</small>

## NVM

[NVM](https://github.com/creationix/nvm)

충돌을 피하기 위해 NVM을 설치하기 전 기존에 설치한 버전의 Node.js는 제거하는 것이 좋습니다.<small>하지만 본인은 그대로 진행했다는거, 따라했다가 잘못되어도 내 탓 아님</small>
NVM을 설치하거나 업데이트를 하려면 [cURL](https://ko.wikipedia.org/wiki/CURL)로 설치 스크립트를 사용할 수 있습니다.
```bash
$ curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash
```
혹은 Homebrew로 설치할 수 있습니다.
```bash
$ brew install nvm
```
설치가 되면 `~/.bash_profile`,`~/.zshrc`,`~/.proflie`등의 프로파일에 `nvm.sh`이 실행되도록 다음 스크립트가 추가됩니다.
```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
```
혹시 추가되지 않았다면 직접 추가합니다.
```bash
# Node 버전 설치  
$ nvm install <version>  # ex> nvm install 8.9.4

# 설치된 Node 버전 목록 확인
$ nvm ls  

# 사용할 Node 설정  
$ nvm use <version>  # ex> nvm use 8.9.4  
$ nvm use <alias>  # ex> nvm use default

# 사용할 alias 설정
$ nvm alias <alias> <version>  # ex> nvm alias test-v 8.9.4
```

추가 [사용법(Usage)](https://github.com/nvm-sh/nvm#usage-1)

---

## n

n은 기존에 설치된 Node.js를 제거할 필요가 없기 때문에 좀 더 쉽게 설치할 수 있습니다.<br />
npm은 전역(Global) 설치합니다.

```bash
$ npm install -g n

# 관리자 권한을 요구할 경우
$ sudo npm install -g n
```
간단한 사용법을 소개하겠습니다.<br />관리자 군한을 요구할 경우(`Error: sudo required`) 앞에 `sudo`를 붙입니다. 또한 제거(rm)할 경우에도 필요할 수 있습니다.
```bash
# 설치된 Node 버전 사용(목록에서 선택 후 Ctrl + c)
$ n

# 모든 Node 버전 중 설치된 버전 확인
$ n ls  

# Node 버전 설치  
$ n <version>  # ex> n 8.9.4
$ n latest  # 최신 LTS Node 버전 설치

# 제거할 Node 설정
$ n rm <version ...>  #ex> n rm 8.9.1 8.9.2
$ n prune  # 현재 버전을 제외한 모든 버전 제거
```
추가 [사용법(Usage)](https://github.com/tj/n#usage)