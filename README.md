파일생성
# uv init 
폴더 이동
# cd 폴더명


설치
# uv add streamlit

실행
# uv run streamlit hello

uv로 파일 실행 
# uv run streamlit run main.py 

패키지 설치(의존성 추가)
# uv add pandas matplotlib streamlit lxml 이렇게도 추가 가능
# uv add lxml
# uv add matplotlib
# uv add pandas
# uv add streamlit


| gotham | pixel | 
|:-----:|:--------:|
| [<img src="https://github.com/ShellStudy/gotham/raw/main/images/gotham.webp" width="80" alt="고담팀"/>](https://github.com/CHOIBEAR) | [<img src="https://cdn.discordapp.com/attachments/1369469538168475698/1398210960216559696/5faeb2d562dbc107.png?ex=68d3a2ee&is=68d2516e&hm=474582e419e22a9ed1438a8602f67431d61b4b4b23f0d247fb11517e5c69ee36&" width="80" alt="픽셀팀"/>](https://github.com/hiedupixel) 
| [고담](https://github.com/higotham) | [픽셀](https://github.com/hiedupixel) 



## Generating Asymmetric Keys with OpenSSL
1. [windows openssl 설치]("https://slproweb.com/products/Win32OpenSSL.html")
2. openssl 버젼 확인
```cmd
openssl -v
```
3. Generate a KeyPair
```cmd
openssl genrsa -out keypair.pem 2048
```
4. Generate a Public Key
```cmd
 openssl rsa -in keypair.pem -pubout -out publicKey.pem 
```
5. Generate a Private Key
```cmd
openssl pkcs8 -topk8 -inform PEM -outform PEM -nocrypt -in keypair.pem -out privateKey.pem
```
6. Spring boot : `properties` 생성
```
@ConfigurationProperties(prefix = "jwt")
 public record RSAKeyRecord (
  RSAPublicKey rsaPublicKey, RSAPrivateKey rsaPrivateKey
 ) {}
```
7. 등록한 Properties 활성화 적용하기
```
@EnableConfigurationProperties(RSAKeyRecord.class)
@SpringBootApplication
public class SpringSecurityApplication {

    public static void main(String[] args) {
        SpringApplication.run(SpringSecurityApplication.class, args);
    }

}
```
8. Location of file in properties
```yml
jwt:
  rsa-private-key: classpath:certs/privateKey.pem
  rsa-public-key: classpath:certs/publicKey.pem
```
9. Jwt 설정 적용하기
```java
@Configuration
@RequiredArgsConstructor
public class JwtConfig {

  private final RsaKeyProperties rsaKeys;

  @Bean
  public JwtEncoder jwtEncoder() {
    JWK jwk = new RSAKey.Builder(rsaKeys.publicKey()).privateKey(rsaKeys.privateKey()).build();
    JWKSource<SecurityContext> jwks = new ImmutableJWKSet<>(new JWKSet(jwk));
    return new NimbusJwtEncoder(jwks);
  }

  @Bean
  public JWKSet jwkSet() {
    RSAKey.Builder builder = new RSAKey.Builder(rsaKeys.publicKey())
        .keyUse(KeyUse.SIGNATURE)
        .algorithm(JWSAlgorithm.RS256)
        .keyID("public-key-id");
    return new JWKSet(builder.build());
  }

  @Bean
  public JwtDecoder jwtDecoder() {
      JWKSource<SecurityContext> jwkSource = new ImmutableJWKSet<>(jwkSet());
      return new NimbusJwtDecoder(jwkSource);
  }

}
```
10. JwkDecoder 를 위한 jwkSet 요청 URI 생성
```java
@RestController
@RequiredArgsConstructor
public class JwkSetController {

  private final JWKSet jwkSet;

  @GetMapping("/.well-known/jwks.json")
  public Map<String, Object> keys() {
    return jwkSet.toJSONObject();
  }

}
```
11. jwkSet 요청 URI를 이용하여 JwkDecoder 하는 Bean 생성
```java
public class SecurityConfig {

  private String jwkSetURI = "/.well-known/jwks.json";

  @Bean
  public JwtDecoder jwtDecoder() {
    return NimbusJwtDecoder.withJwkSetUri(jwkSetURI).build();
  }

}
```


| Unnamed: 0    | Unnamed: 1      | Unnamed: 2           | Unnamed: 3            | Unnamed: 4   | Unnamed: 5            | Unnamed: 6   | Unnamed: 7   | Unnamed: 8               | Unnamed: 9          | Unnamed: 10        | Unnamed: 11    | Unnamed: 12              | Unnamed: 13      | Unnamed: 14        | Unnamed: 15                | Unnamed: 16   | Unnamed: 17     |
|:--------------|:----------------|:---------------------|:----------------------|:-------------|:----------------------|:-------------|:-------------|:-------------------------|:--------------------|:-------------------|:---------------|:-------------------------|:-----------------|:-------------------|:---------------------------|:--------------|:----------------|
| 프로젝트      | 기능            | 상세기능             | 화면                  | nan          | Controller            | nan          | nan          | nan                      | nan                 | Service            | nan            | nan                      | nan              | Repository(Mapper) | nan                        | nan           | nan             |
| nan           | nan             | nan                  | URL                   | METHO        | CLASS                 | role         | METHOD       | PARAMETER                | RETURN              | CLASS              | METHOD         | PARAMETER                | RETURN           | CLASS              | METHOD                     | SQL           | RETURN          |
| solo          | 홈페이지(화면)  | 프론트 화면          | /                     | GET          | HomeController        | -            | -            | -                        | String              | nan                | nan            | nan                      | nan              | nan                | nan                        | nan           | nan             |
| nan           | 차트(계정)      | 그래프로 사용자 확인 | /data                 | GET          | nan                   | nan          | data         | nan                      | ResponseDTO         | nan                | nan            | nan                      | nan              | DataMapper         | findAllUser                | -             | List<ResultDTO> |
| nan           | 차트(파일)      | 그래프로 파일 확인   | nan                   | nan          | nan                   | nan          | nan          | nan                      | nan                 | nan                | nan            | nan                      | nan              | nan                | findAllFile                | nan           | nan             |
| authorization | 사용자정보      | 사용자 삭제          | /user                 | DELETE       | UserController        | 로그인필수   | delete       | authentication           | ResDTO              | UserService        | delete         | authentication           | ResDTO           | UserRepository,    | -                          | delete        | UserEntity      |
|               |                 |                      |                       |              |                       |              |              |                          |                     |                    |                |                          |                  | RoleRepository,    |                            |               |                 |
|               |                 |                      |                       |              |                       |              |              |                          |                     |                    |                |                          |                  | RoleUserRepository |                            |               |                 |
| nan           | nan             | 사용자 조회          | /user                 | GET          | nan                   | 로그인필수   | userInfo     | authentication           | nan                 | nan                | userInfo       | authentication           | nan              | nan                | -                          | select        | UserEntity      |
| nan           | nan             | 사용자 수정          | /user                 | PATCH        | nan                   | 로그인필수   | modify       | userInfoReqDTO,          | nan                 | nan                | modify         | userInfoReqDTO,          | nan              | nan                | -                          | update        | UserEntity      |
|               |                 |                      |                       |              |                       |              |              | authentication           |                     |                    |                | authentication           |                  |                    |                            |               |                 |
| nan           | nan             | 로그인               | /user                 | POST         | nan                   | -            | signIn       | authReqDTO,              | nan                 | nan                | signIn         | authReqDTO,              | nan              | nan                | signInfindByEmailAndUseYn, | select        | UserEntity      |
|               |                 |                      |                       |              |                       |              |              | request,                 |                     |                    |                | request,                 |                  |                    | findByEmail                |               |                 |
|               |                 |                      |                       |              |                       |              |              | response,                |                     |                    |                | response,                |                  |                    |                            |               |                 |
|               |                 |                      |                       |              |                       |              |              | session                  |                     |                    |                | session                  |                  |                    |                            |               |                 |
| nan           | nan             | 로그아웃             | /user/logout          | POST         | nan                   | -            | logout       | request,                 | nan                 | nan                | logout         | request,                 | nan              | nan                | -                          | -             | -               |
|               |                 |                      |                       |              |                       |              |              | response                 |                     |                    |                | response                 |                  |                    |                            |               |                 |
| nan           | nan             | 이메일 인증          | /user/email           | POST         | nan                   | -            | email        | userDto                  | nan                 | nan                | email          | userDto                  | nan              | nan                | -                          | select        | UserEntity      |
| nan           | nan             | 이메일 인증번호      | /user/auth            | POST         | nan                   | -            | auth         | authReqDTO               | nan                 | nan                | auth           | authReqDTO               | nan              | nan                | -                          | -             | -               |
| nan           | nan             | 회원가입             | /user                 | PUT          | nan                   | -            | signUp       | userDto                  | nan                 | nan                | signUp         | userDto                  | nan              | nan                | -                          | insert        | UserEntity      |
| nan           | 파일관리        | 파일다운로드/조회    | /file/{type}/{no}     | GET          | FileController        | -            | uri          | type, no, authentication | ResponseEntity      | FileService        | uri            | type, no, authentication | ResponseEntity   | FileRepository,    | findByNoAndUseYn           | update        | FileEntity      |
|               | (AI 생성이미지) |                      |                       |              |                       |              |              |                          |                     |                    |                |                          |                  | userRepository     |                            |               |                 |
| nan           | nan             | 파일다운로드/조회    | /file/{no}            | GET          | nan                   | 로그인필수   | uri          | no, authentication       | nan                 | nan                | uri            | no, authentication       | nan              | nan                | findByNoAndUseYn           | update        | FileEntity      |
| nan           | nan             | 파일업로드           | /file                 | POST         | nan                   | 로그인필수   | upload       | file, authentication     | ResDTO              | nan                | upload         | file, authentication     | ResDTO           | nan                | findById                   | select        | FileEntity      |
| nan           | OAuth관리       | 홈엔드포인트         | /                     | GET          | OAuthClientController | -            | home         | authentication           | String              | OAuthClientService | findById       | id                       | RegisteredClient | userRepository     | -                          | select        | UserEntity      |
| nan           | nan             | JWK public key 조회  | /.well-known/jws.json | GET          | nan                   | -            | keys         | -                        | Map<String, Object> | nan                | findByClientId | clientId                 | RegisteredClient | nan                | findByEmailAndUseYn        | select        | UserEntity      |
| gateway       | nan             | nan                  | nan                   | nan          | nan                   | nan          | nan          | nan                      | nan                 | nan                | nan            | nan                      | nan              | nan                | nan                        | nan           | nan             |
