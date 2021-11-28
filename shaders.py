# Universidad del Valle de Guatemala
# Priscilla González - 20689
# Proyecto 4 OGL - Gráficas

# GLSL
# Graphics Library Shaders Library

# uniform todos los vértices usan el mismo valor
# layout cambian de valor por cada vértice

vertex_shader = """
#version 450
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoords;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float tiempo;
uniform float valor;
uniform vec3 pointLight;

out vec3 outColor;
out vec2 outTexCoords;

void main()
{
    vec4 norm = vec4(normal, 0.0);
    vec4 pos = vec4(position, 1.0) + norm * valor;
    pos = modelMatrix * pos;
    vec4 light = vec4(pointLight, 1.0);
    float intensity = dot(modelMatrix * norm, normalize(light - pos));
    gl_Position = projectionMatrix * viewMatrix * pos;
    outColor = vec3(1.0,1.0 - valor * 2,1.0-valor * 2) * intensity;
    outTexCoords = texCoords;
}
"""

fragment_shader = """
#version 450
layout (location = 0) out vec4 fragColor;
in vec3 outColor;
in vec2 outTexCoords;
uniform sampler2D tex;
void main()
{
    fragColor = vec4(outColor, 1) * texture(tex, outTexCoords);
}
"""

toon_vertex_shader = """
#version 450
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoords;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float tiempo;
uniform float valor;
uniform vec3 pointLight;

out vec2 outTexCoords;
out float intensity;

void main()
{
    vec4 norm = vec4(normal, 0.0);
    vec4 pos = vec4(position, 1.0) + norm * valor;
    pos = modelMatrix * pos;
    vec4 light = vec4(pointLight, 1.0);
    intensity = dot(modelMatrix * norm, normalize(light - pos));
    gl_Position = projectionMatrix * viewMatrix * pos;
    outTexCoords = texCoords;
}
"""

toon_fragment_shader = """
#version 450
layout (location = 0) out vec4 fragColor;
in vec2 outTexCoords;
in float intensity;
uniform sampler2D tex;
void main()
{
    if (intensity > 0.95)            {fragColor = vec4(0.73, 1.00, 0.00, 1) * intensity;}
    else if (intensity > 0.75)       {fragColor = vec4(0.62, 0.77, 0.20, 1) * intensity;}
    else if (intensity > 0.50)       {fragColor = vec4(0.52, 0.61, 0.27, 1) * intensity;}
    else if (intensity > 0.25)       {fragColor = vec4(0.40, 0.45, 0.26, 1) * intensity;}
    else                             {fragColor = vec4(0.28, 0.30, 0.22, 1) * intensity;}
}
"""

negative_fragment_shader = """
#version 450
layout (location = 0) out vec4 fragColor;

in vec2 outTexCoords;
in float intensity;

void main()
{

    fragColor = vec4(1.0, 0.0, 0.0, 1.0);
    fragColor = vec4(0.0, 1.0, 0.0, 1.0);
    fragColor = vec4(0.0, 0.0, 1.0, 1.0); 

    if (intensity > 0.0) {fragColor = (1.0 - vec4(1.0, 0.0, 0.0, 1)) * intensity, (1.0 - vec4(0.0, 1.0, 0.0, 1)) * intensity, (1.0 - vec4(0.0, 0.0, 1.0, 1)) * intensity;}
    else                 {fragColor = vec4(1.0, 1.0, 1.0, 1.0) * intensity;}
}
"""

trigonometric_fragment_shader = """
#version 450
layout (location = 0) out vec4 fragColor;

in vec2 outTexCoords;
in float intensity;

#define pi 3.14159265359
void main()
{
    float r = sin(outTexCoords.x * pi * 15);
    float g = sin(outTexCoords.y * pi * 10);
    float b = 1.0;

    fragColor = vec4(r, g, b, 1.0) * intensity;
}
"""

rad_fragment_shader = """
#version 450
layout (location = 0) out vec4 fragColor;

in vec2 outTexCoords;
in float intensity;

#define pi 3.14159265359
void main()
{
    vec2 var = vec2(0.5) - outTexCoords;

    float rad = length(var) * 1;
    float angle = atan(var.x, var.y);

    float r = 1.0;
    float g = sin(angle * pi * 15);
    float b = sin(rad * pi * 20);

    fragColor = vec4(r, g, b, 1.0) * intensity;
}
"""

flower_fragment_shader = """
#version 450
layout (location = 0) out vec4 fragColor;

in vec2 outTexCoords;
in float intensity;

#define pi 3.14159265359
void main()
{
    vec2 var = vec2(0.5) - outTexCoords;

    float rad = length(var) * 1;
    float angle = atan(var.x, var.y);

    float r = 1.0;
    float g = 1.0 + cos(angle);
    float b = sin(rad * pi * 20 + sin(angle * 15));

    fragColor = vec4(r, g, b, 1.0) * intensity;
}
"""