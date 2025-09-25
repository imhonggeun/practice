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
| [<img src="https://cdn.discordapp.com/attachments/1369469538168475698/1398152935296467116/f7a166b44f5fbafa.png?ex=68d36ce4&is=68d21b64&hm=564b0905924712db6f25fc7b68895bb4b5a75b95ccbaf00ff11fff052584dc82&" width="80" alt="고담팀"/>](https://github.com/CHOIBEAR) | [<img src="https://cdn.discordapp.com/attachments/1369469538168475698/1398210960216559696/5faeb2d562dbc107.png?ex=68d3a2ee&is=68d2516e&hm=474582e419e22a9ed1438a8602f67431d61b4b4b23f0d247fb11517e5c69ee36&" width="80" alt="픽셀팀"/>](https://github.com/hiedupixel) 
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
