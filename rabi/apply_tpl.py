# -*- mode: python -*-
# -*- coding: utf-8 -*-

from jinja2 import Template

template_editorconfig = """\
root = true


[*]
end_of_line = lf
insert_final_newline = true
charset = utf-8
indent_style = space
indent_size = 2


[{*.json,.babelrc,travis.yml}]
indent_size = 4

"""

template_flowconfig = """\
[ignore]
.*\.config\.js
<PROJECT_ROOT>/dist/.*
<PROJECT_ROOT>/tests/.*


[include]


[libs]


[options]
module.ignore_non_literal_requires=true

"""

template_babelrc = """\
{
    "presets": ["react", ["env", {
        "target": {
            "node": true
        },
        "modules": false,
        "loose": true
    }]],
    "plugins": [
        ["transform-object-rest-spread", { "useBuiltIns": true } ],
        "transform-class-properties",
        "lodash"
    ],
    "env": {
        "test": {
            "plugins": ["transform-es2015-modules-commonjs"]
        }
    }
}

"""

template_gitignore = """\
# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Directory for instrumented libs generated by jscoverage/JSCover
lib-cov

# Coverage directory used by tools like istanbul
coverage

# nyc test coverage
.nyc_output

# Grunt intermediate storage (http://gruntjs.com/creating-plugins#storing-task-files)
.grunt

# Bower dependency directory (https://bower.io/)
bower_components

# node-waf configuration
.lock-wscript

# Compiled binary addons (http://nodejs.org/api/addons.html)
build/Release

# Dependency directories
node_modules/
jspm_packages/

# Typescript v1 declaration files
typings/

# Optional npm cache directory
.npm

# Optional eslint cache
.eslintcache

# Optional REPL history
.node_repl_history

# Output of 'npm pack'
*.tgz

# Yarn Integrity file
.yarn-integrity

# dotenv environment variables file
.env

# Flowtype
flow-bin
flow-typed/npm

# Build directory
dist

"""

template_packagejson = """\
{
    "name": "{{pkg_name}}",
    "version": "0.0.1",
    "main": "dist/{{name}}.js",
    "npmName": "{{global_name}}",
    "repository": "git@github.com:yuffiy/{{name}}.git",
    "author": "Rabbit <yfhj1990@hotmail.com>",
    "license": "GPL-3.0",
    "devDependencies": {
        "babel-core": "^6.26.0",
        "babel-jest": "^21.0.2",
        "babel-plugin-lodash": "^3.2.11",
        "babel-plugin-transform-class-properties": "^6.24.1",
        "babel-plugin-transform-object-rest-spread": "^6.26.0",
        "babel-preset-env": "^1.6.0",
        "babel-preset-react": "^6.24.1",
        "enzyme": "^2.9.1",
        "flow-bin": "^0.54.1",
        "history": "^4.7.2",
        "jest": "^21.1.0",
        "lodash": "^4.17.4",
        "react": "^15.6.1",
        "react-addons-test-utils": "^15.6.0",
        "react-dom": "^15.6.1",
        "react-router": "^4.2.0",
        "react-router-dom": "^4.2.2",
        "react-test-renderer": "^15.6.1",
        "rollup": "^0.50.0",
        "rollup-plugin-babel": "^3.0.2",
        "rollup-plugin-uglify": "^2.0.1"
    },
    "dependencies": {
        "rabbit-lazy-component": "^0.0.5",
        "rabbit-promise-extra": "^0.0.7"
    },
    "peerDependencies": {
        "react": ">= 14",
        "react-router-dom": ">= 4"
    },
    "files": [
        "dist",
        "lib"
    ],
    "scripts": {
        "test": "jest",
        "typed": "flow",
        "checkall": "yarn test && yarn typed",
        "build:umd": "cross-env NODE_ENV=development rollup -c",
        "build:umd:min": "cross-env NODE_ENV=production rollup -c",
        "build": "yarn build:umd && yarn build:umd:min"
    }
}

"""

template_rollupconfig = """
import startCase from 'lodash/startCase'
import babel     from 'rollup-plugin-babel'
import uglify    from 'rollup-plugin-uglify'
import pkg       from './package.json'

const input     = 'lib/index.js'
const name      = startCase(pkg.npmName).replace(/\s/g, '')
const format    = 'umd'
const sourcemap = true
const globals = {
  {%- for key, value in global_exports.items() %}
  {{key}}: {{value}}{% if not loop.last %},{% endif %}
  {%- endfor %}
}

let output, plugins = [ babel() ]


if(process.env.NODE_ENV === 'development') {
  output = {
    file: 'dist/{{name}}.js',
    format,
    sourcemap
  }
} else {
  output = {
    file: 'dist/{{name}}.min.js',
    format,
    sourcemap
  }

  plugins.push(uglify())
}

export default  {
  input,
  output,
  name,
  plugins,
  globals  
}

"""


if __name__ == '__main__':
    tpl = Template(template_rollupconfig)
    print(tpl.render(global_exports={'foo': 'bar', 'baz': 'qux'}))
